import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { BasketComponent } from './basket/basket.component';

export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'cart', component: BasketComponent },
];
