import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../models';
import { ActivatedRoute } from '@angular/router';
import { CompanyService } from '../company.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-vacancy',
  templateUrl: './vacancy.component.html',
  standalone: true,
  styleUrls: ['./vacancy.component.css'],
  imports: [
    RouterModule,
    CommonModule,
  ]
})
export class VacancyComponent implements OnInit {
  vacancies: Vacancy[] = [];
  constructor(private route: ActivatedRoute, private companyService: CompanyService) {}

  ngOnInit(): void {
    this.getCompanyVacancies();
  }

  getCompanyVacancies(): void {
    this.route.paramMap.subscribe(params => {
      const idString = params.get('id');
      if (idString !== null) {
        const id = +idString;
        this.companyService.getCompanyVacancies(id).subscribe(data => {
          this.vacancies = data;
        });
      } else {
        // Обработка ситуации, когда id отсутствует в URL
      }
    });
  }
  
}
