import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { products } from '../products';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit{
  
  public categoryId: number = 0

  constructor(private route: ActivatedRoute){ }

  ngOnInit() {
    const routep = this.route.snapshot.paramMap;
    this.categoryId = Number(routep.get('categoryId'));
      
  }

  

 
}