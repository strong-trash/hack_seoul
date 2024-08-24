import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { scene } from './scene/scene.component';
import { CartComponent } from './cart/cart.component';

@NgModule({
  declarations: [AppComponent, CartComponent, scene],
  imports: [BrowserModule, CartComponent, scene],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
