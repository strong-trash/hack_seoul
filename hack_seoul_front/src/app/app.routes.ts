import { Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { CartComponent } from './cart/cart.component';
import { scene } from './\bscene/scene.component';
export const routes: Routes = [
  { path: '', component: AppComponent },
  { path: 'scene', component: scene },
  { path: 'cart', component: CartComponent },
];
