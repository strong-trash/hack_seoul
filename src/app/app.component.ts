import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { maincoupang } from './main/maincoupang.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, maincoupang],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css',
})
export class AppComponent {
  title = 'coupang_match';
}
