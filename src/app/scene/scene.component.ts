import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import Swiper from 'swiper';
import { Navigation, Pagination, Mousewheel } from 'swiper/modules';
import { API } from '../AxiosRestApi';
@Component({
  selector: 'main-coupang',
  standalone: true,
  imports: [FormsModule, CommonModule],
  templateUrl: './scene.component.html',
  styleUrl: './scene.component.css',
})
export class scene implements OnInit {
  api: API = new API();
  isDrag: boolean = false;
  swiper: Swiper | undefined;
  test: String = '';
  startX: number = 0;
  itemId: number = 0;
  formerItemId: number = 0;
  slides: any[] = [];

  ngOnInit(): void {}
  ngAfterViewInit() {
    this.api.getProduct(this.itemId).then((res: any) => {
      this.slides.push(res.data);
      this.itemId = res.data.id;
      this.api.getProduct(this.itemId).then((res: any) => {
        this.slides.push(res.data);
        this.itemId = res.data.id;
        this.api.getProduct(this.itemId).then((res: any) => {
          this.slides.push(res.data);
          this.itemId = res.data.id;
          this.swiper = new Swiper('.swiper-container', {
            modules: [Navigation, Pagination, Mousewheel],
            direction: 'vertical',
            slidesPerView: 1,
            spaceBetween: 30,
            mousewheel: true,
            pagination: {
              el: '.swiper-pagination',
              clickable: true,
            },
            navigation: {
              nextEl: '.swiper-button-next',
              prevEl: '.swiper-button-prev',
            },
            on: {
              touchStart: (swiper, event) => {
                // Record starting position
                if (event instanceof TouchEvent) {
                  this.startX = event.touches[0].clientX;
                } else {
                  this.startX = event.clientX;
                }
              },
              touchMove: (swiper, event) => {
                let currentX: number = 0;

                if (event instanceof MouseEvent) {
                  currentX = event.clientX;
                } else if (event instanceof TouchEvent) {
                  currentX = event.changedTouches[0].clientX;
                }

                const deltaX = currentX - this.startX;
                const sceneElement = document.querySelector(
                  '.scene'
                ) as HTMLElement;
                sceneElement.style.transform = `translateX(${deltaX * 10}px)`;
              },
              touchEnd: (swiper, event) => {
                let lastX = 0;
                if (event instanceof MouseEvent) {
                  lastX = event.clientX;
                } else if (event instanceof TouchEvent) {
                  lastX = event.changedTouches[0].clientX;
                }
                const result = this.startX - lastX;
                if (result > 100) {
                  //left
                } else if (result <= -100) {
                  //right
                }
                this.startX = 0;
                const sceneElement = document.querySelector(
                  '.scene'
                ) as HTMLElement;
                sceneElement.style.transition =
                  'transform 0.5s cubic-bezier(0.22, 1, 0.36, 1)'; // Bouncy effect
                sceneElement.style.transform = `translateX(0px)`;
              },
              slideChangeTransitionEnd: (swiper) => {
                console.log(swiper.swipeDirection);
                swiper.update();
                if (swiper.swipeDirection == 'next') {
                  this.api.getProduct(this.itemId).then((res: any) => {
                    this.slides.push(res.data);
                    this.itemId = res.data.id;
                  });
                }
              },
            },
          });
        });
      });
    });
  }
}
