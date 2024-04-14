import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./pages/home/home.module').then(m => m.HomeModule),
  },
  { 
    path: 'churn-years', 
    loadChildren: () => import('./pages/analytics/analytics.module').then(m => m.AnalyticsModule),
  },
  { 
    path: 'analytics-clients', 
    loadChildren: () => import('./pages/analytics-clients/analytics-clients.module').then(m => m.AnalyticsClientsModule),
  },
  { 
    path: 'upload', 
    loadChildren: () => import('./pages/upload/upload.module').then(m => m.UploadModule),
  },

];
