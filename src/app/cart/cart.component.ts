import { Component, OnInit } from '@angular/core';
import { API } from '../AxiosRestApi';
import { CommonModule, Location } from '@angular/common';

@Component({
  selector: 'app-cart',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './cart.component.html',
  styleUrl: './cart.component.css',
})
export class CartComponent implements OnInit {
  productList: any[] = [];
  api: API = new API();
  constructor(private location: Location) {}
  goBack = () => {
    this.location.back();
  };
  ngOnInit(): void {
    this.api.getCart(1).then((res) => {
      console.log(res);
      this.productList.push(...res.data.products);
    });
  }
}
