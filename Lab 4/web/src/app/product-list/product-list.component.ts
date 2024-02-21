import { Component } from '@angular/core';

import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  products = [...products];

  sharewhatsapp(name:string, link:string) {
    const whatsappUrl = `https://api.whatsapp.com/send?text=${encodeURIComponent(name + ': ' + link)}`;
    window.open(whatsappUrl, '_blank');

  }
  sharetelegram(name:string, link:string) {
    const telegramUrl = `https://t.me/share/url?url=${encodeURIComponent(link)}&text=Купить ${encodeURIComponent(name)}`;
    window.open(telegramUrl, '_blank');
  }
  onNotify() {
    window.alert('You will be notified when the product goes on sale');
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/