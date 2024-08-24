import { Component } from '@angular/core';
import { Router, RouterOutlet } from '@angular/router';
import { scene } from './scene/scene.component';
import { CartComponent } from './cart/cart.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, scene, CartComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  constructor(private router: Router) {
    this.router.navigate(['scene']);
  }
}
