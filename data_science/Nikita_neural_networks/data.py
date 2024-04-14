from datetime import datetime
import pandas as pd
import polars as pl
import numpy as np
import torch
from tqdm.auto import tqdm 


def get_data_period(agg_df, 
                    trnsc_df,
                    start_year,
                    target_year):
    #Filter train_df dataset with aggregations
    start_date_mask_agg = agg_df['year'] >= start_year
    end_date_mask_agg = agg_df['year'] < target_year
    filtered_agg_df = agg_df[start_date_mask_agg & end_date_mask_agg]
    # Filter transcations_df 
    start_date_mask_trans = trnsc_df['year'] >= start_year
    end_date_mask_trans = trnsc_df['year'] < target_year
    filtered_trnsc_df = trnsc_df[start_date_mask_trans & end_date_mask_trans]
    # Getting 4 targets for each unique user and contract in end_date year
    targets = agg_df[agg_df['year'] == target_year]
    # Split on each quarter
    temp_mask_q1 = targets['quarter'].str
    target_list = [targets[targets['quarter'].str.contains(f'Q{i}')] for i in range(1, 5)]

    return filtered_agg_df, filtered_trnsc_df, target_list

def read_data(path, sep=None):
    if sep is not None:
        df = pd.read_csv(path, sep=sep)
    else:
        df = pd.read_csv(path)
    display(path, df.shape, df.head(3))
    display(df.isna().sum())
    
    return df


def print_info(df):
    display(df.head(2))
    min_year, max_year = df['year'].min(), df['year'].max()
    print(f'min year: {min_year}, max year: {max_year}')
    

def print_info_targets(list_df):
    for i in range(len(list_df)):
        min_year, max_year = list_df[i]['year'].min(), list_df[i]['year'].max() 
        display(list_df[i]['quarter'].unique(), f'min, max year = ')

def read_data(path, sep=None):
    if sep is not None:
        df = pd.read_csv(path, sep=sep)
    else:
        df = pd.read_csv(path)
    #display(path, df.shape, df.head(3))
    #display(df.isna().sum())
    
    return df
        
def prepare_dataset(path):
    print('Reading file')
    train_df = pl.read_csv(path)
    print('End of Reading file')
    
    def preprocess_df(df):
        df = df.to_pandas()
        df['npo_oprtn_date'] = pd.to_datetime(df['npo_oprtn_date'])
        df.rename(columns={'target_year': 'tyear', 'cat_year': 'year'}, inplace=True)
        return df
    
    print('Process dataframe')
    pd_train_df = preprocess_df(train_df)
    selected_col = ['npo_sum', 'quarter', 'year', 'target_churn','npo_account_id', 'tyear', 'target_quarter']
    print('Groupby dataframe')
    grouped = pd_train_df[selected_col].groupby(['npo_account_id', 'tyear', 'target_quarter']).agg(lambda x: x.tolist()).reset_index()
    records = grouped.to_dict(orient='records')
    for rec in tqdm(records):
        event_time = [i for i in range(len(rec['npo_sum']))]
        rec['event_time'] = torch.tensor(event_time)
        for col in rec:
            if col == 'target_churn':
                rec['target_churn'] = rec['target_churn'][-1] 
            if col == 'quarter' or col == 'year':
                rec[col] = torch.LongTensor(rec[col])
            if col == 'npo_sum':
                rec[col] = torch.tensor(rec[col])
                
    print(rec)
    selected_col  = ['quarter', 'year']
    cat_to_unique_size = {
        col: pd_train_df[col].unique().shape[0] for col in selected_col
    }

    print(cat_to_unique_size)
    return records