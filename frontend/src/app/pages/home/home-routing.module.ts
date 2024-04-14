import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
  },
  {
    path: 'churn-years',
    loadChildren: () => import('../analytics/analytics.module').then(m => m.AnalyticsModule)
  },
  { 
    path: 'analytics-clients', 
    loadChildren: () => import('../analytics-clients/analytics-clients.module').then(m => m.AnalyticsClientsModule),
  },
  {
    path: 'upload',
    loadChildren: () => import('../upload/upload.module').then(m => m.UploadModule)
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class HomeRoutingModule { }