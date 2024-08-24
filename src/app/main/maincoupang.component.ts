import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import Swiper from 'swiper';
@Component({
  selector: 'main-coupang',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './maincoupang.component.html',
  styleUrl: './maincoupang.component.css',
})
export class maincoupang {
  test = '';
  slides = [
    { id: 1, content: 'Slide 1 Content' },
    { id: 2, content: 'Slide 2 Content' },
    { id: 3, content: 'Slide 3 Content' },
  ];
  onClick = () => {
    this.test = 'clicked';
  };
}
