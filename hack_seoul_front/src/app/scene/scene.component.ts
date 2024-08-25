import { CommonModule } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { FormsModule } from '@angular/forms';
import Swiper from 'swiper';
import { Navigation, Pagination, Mousewheel } from 'swiper/modules';
import { API } from '../AxiosRestApi';
import { Router, RouterOutlet } from '@angular/router';
@Component({
  selector: 'main-coupang',
  standalone: true,
  imports: [FormsModule, CommonModule, RouterOutlet],
  templateUrl: './scene.component.html',
  styleUrl: './scene.component.css',
})
export class scene implements OnInit {
  api: API = new API();
  swiper: Swiper | undefined;
  startX: number = 0;
  itemId: number = 0;

  slides: any[] = [];
  dislikeClassList: string = '';
  likeClassList: string = '';
  constructor(private router: Router) {}
  KRWon = new Intl.NumberFormat('ko-KR', {
    style: 'currency',
    currency: 'KRW',
  });

  // wonjin lee - start
  curSlideIdx: number = 0;
  curSlideLikeCount: number = 0;
  curSlideDislikeCount: number = 0;
  curSlideIsLike: boolean = false;
  curSlideIsDislike: boolean = false;
  isLoading: boolean = false;
  updateCurCount = async () => {
    this.isLoading = true;

    try {
      console.log('---');
      const { data } = await this.api.getProduct(this.curSlideIdx, 1);
      console.log(data);
      this.curSlideLikeCount = data.like_count;
      this.curSlideDislikeCount = data.dislike_count;
      this.curSlideIsLike = data.is_like;
      this.curSlideIsDislike = data.is_dislike;
      console.log(this.curSlideLikeCount, this.curSlideDislikeCount);
    } finally {
      this.isLoading = false;
    }
  };
  // wonjin lee - end

  // like = (proId: number, usrId: number, slide: any) => {
  like = async (proId: number, usrId: number, slide: any) => {
    this.api.like(proId, usrId);
    slide.is_like = true;
    slide.is_dislike = false;

    // wonjin lee - start
    await this.updateCurCount();
    // wonjin lee - end
  };

  dislike = async (proId: number, usrId: number, slide: any) => {
    this.api.dislike(proId, usrId);
    slide.is_like = false;
    slide.is_dislike = true;

    // wonjin lee - start
    await this.updateCurCount();
    // wonjin lee - end
  };

  isLike(slide: any) {
    return slide.is_like ? 'selected' : '';
  }
  isDisLike(slide: any) {
    return slide.is_dislike ? 'selected' : '';
  }
  // wonjin lee - start
  showBackdrop(isLoading: boolean) {
    console.log(isLoading);
    return isLoading ? 'show-backdrop' : 'hide-backdrop';
  }
  // wonjin lee - end

  ngOnInit(): void {}
  ngAfterViewInit() {
    this.api.getProduct(this.itemId, 1).then((res: any) => {
      res.data.price = this.KRWon.format(res.data.price);
      this.slides.push(res.data);
      this.itemId = res.data.id;
      this.api.getProduct(this.itemId, 1).then((res: any) => {
        res.data.price = this.KRWon.format(res.data.price);
        this.slides.push(res.data);
        this.itemId = res.data.id;
        this.api.getProduct(this.itemId, 1).then((res: any) => {
          res.data.price = this.KRWon.format(res.data.price);
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
                  this.router.navigate(['cart']);
                } else if (result <= -100) {
                  //right
                  if (this.swiper) {
                    const id = this.slides[this.swiper.activeIndex].id;
                    this.api.addCart(1, id);
                    this.swiper.update();
                    setTimeout(() => {
                      if (this.swiper) this.swiper.slideNext();
                    }, 600);
                  }
                }
                this.startX = 0;
                const sceneElement = document.querySelector(
                  '.scene'
                ) as HTMLElement;
                sceneElement.style.transition =
                  'transform 0.5s cubic-bezier(0.22, 1, 0.36, 1)'; // Bouncy effect
                sceneElement.style.transform = `translateX(0px)`;
              },
              slideChangeTransitionStart: (swiper) => {
                swiper.updateSlides();

                if (swiper.swipeDirection == 'next') {
                  this.api
                    .getProduct(this.itemId, 1)
                    .then((res: any) => {
                      res.data.price = this.KRWon.format(res.data.price);
                      this.slides.push(res.data);
                      swiper.update();
                      this.itemId = res.data.id;
                    })
                    .catch((e) => {
                      console.log(e);
                    });
                }
              },
              slideChangeTransitionEnd: (swiper) => {
                this.swiper?.update();
                // wonjin lee - start
                this.curSlideIdx = swiper.activeIndex;
                console.log(this.curSlideIdx);
                this.updateCurCount();
                // wonjin lee - end
              },
            },
          });
        });
      });
    });
  }
}
