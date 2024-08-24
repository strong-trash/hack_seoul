import axios from 'axios';
export class API {
  link: string =
    'https://6048-2001-2d8-f1b6-b33b-7d30-2a87-264c-d1bb.ngrok-free.app';
  public getProduct = (prodId: number, usrId: number) => {
    let urlLink = this.link.concat('/product');
    if (prodId >= 0 && usrId >= 0) {
      urlLink = urlLink
        .concat('/')
        .concat(prodId.toString())
        .concat('/')
        .concat(usrId.toString());
    }
    return axios.get(urlLink, {
      headers: {
        'Content-Type': `application/json`,
        'ngrok-skip-browser-warning': '69420',
      },
    });
  };
  public like = (prodId: number, usrId: number) => {
    let urlLink = this.link.concat('/like');
    axios
      .post(urlLink, {
        user_id: usrId,
        product_id: prodId,
      })
      .catch((e) => {
        console.log(e);
      });
  };
  public dislike = (prodId: number, usrId: number) => {
    let urlLink = this.link.concat('/dislike');
    axios
      .post(urlLink, {
        user_id: usrId,
        product_id: prodId,
      })
      .catch((e) => {
        console.log(e);
      });
  };
  public getCart = (usrId: number) => {
    let usrLink = this.link.concat('/cart/').concat(usrId.toString());
    return axios.get(usrLink, {
      headers: {
        'Content-Type': `application/json`,
        'ngrok-skip-browser-warning': '69420',
      },
    });
  };
  public addCart = (usrId: number, prodId: number) => {
    let usrLink = this.link.concat('/cart');
    return axios.post(usrLink, {
      user_id: usrId,
      product_id: prodId,
    });
  };
  public updateCart = (cnt: number, cartId: number) => {
    let urlLink = this.link.concat('/cart/').concat(cartId.toString());
    return axios.put(urlLink, {
      count: cnt,
    });
  };
  public delCart = (cartId: number) => {
    let urlLink = this.link.concat('/cart/').concat(cartId.toString());
    return axios.delete(urlLink);
  };
}
