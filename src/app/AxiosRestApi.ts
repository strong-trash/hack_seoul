import axios from 'axios';
export class API {
  link: string =
    'https://6048-2001-2d8-f1b6-b33b-7d30-2a87-264c-d1bb.ngrok-free.app';
  public getProduct = (x: number) => {
    let urlLink = this.link.concat('/product');
    console.log(x);
    if (x >= 0) {
      urlLink = urlLink.concat('/').concat(x.toString());
    }
    return axios.get(urlLink, {
      headers: {
        'Content-Type': `application/json`,
        'ngrok-skip-browser-warning': '69420',
      },
    });
  };
}
