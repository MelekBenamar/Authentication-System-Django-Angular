import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-register',
  standalone: false,
  
  templateUrl: './register.component.html',
  styleUrl: './register.component.css'
})
export class RegisterComponent {
  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router:Router
  ) {
  }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      name: '',
      email: '',
      password: '',
    })
  }

  submit(): void{

    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
    const body = JSON.stringify(this.form.getRawValue());

    this.http.post('http://localhost:8000/api/register/',body, {headers})
      .subscribe(() => this.router.navigate(['/login']))
  }

}
