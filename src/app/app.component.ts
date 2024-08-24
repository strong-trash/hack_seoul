import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { scene } from './scene/scene.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, scene],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {}
