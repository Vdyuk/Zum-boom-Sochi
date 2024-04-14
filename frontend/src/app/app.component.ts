import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, RouterOutlet } from '@angular/router';
import {MatListModule} from '@angular/material/list';
import { Router, NavigationEnd } from '@angular/router';
import {MatIconModule} from '@angular/material/icon';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, MatListModule, RouterModule, MatIconModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent{
  title = 'Зумеры и бумеры';

  list = [
    { name: 'Главная', isActive: true, url: '' },
    { name: 'Клиенты, склонные к оттоку', isActive: false, url: '/analytics-clients' },
    { name: 'Аналитические показатели', isActive: false, url: '/churn-years' },
    { name: 'Загрузка данных', isActive: false, url: '/upload' },
  ];

  constructor(private router: Router) {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        const currentUrl = event.url;
        this.list.forEach(item => {
          item.isActive = item.url === currentUrl;
        });
      }
    });
  }

  scrollToTop() {
    window.scroll({
      top: 0,
      behavior: "smooth",
    });
  }
}
