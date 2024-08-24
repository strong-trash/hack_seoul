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
  addCnt = (item: any) => {
    item.count++;
    this.api.updateCart(item.count, item.id);
  };
  subCnt = (item: any) => {
    if (item.count <= 1) {
      return;
    }
    item.count--;
    this.api.updateCart(item.count, item.id);
  };
  changeCnt = (event: FocusEvent, item: any) => {
    const inputValue = Number((event.target as HTMLInputElement).value);
    if (inputValue < 1) {
      return;
    }
    this.api.updateCart(Number(inputValue), item.id);
  };
  delCart = (item: any) => {
    this.api.delCart(item.id);
    this.productList = this.productList.filter((e) => e.id != item.id);
  };
  ngOnInit(): void {
    this.api.getCart(1).then((res) => {
      console.log(res);
      this.productList.push(...res.data.products);
    });
  }
}
