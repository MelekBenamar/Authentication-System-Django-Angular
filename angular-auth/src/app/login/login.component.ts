import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  standalone: false,
  
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  form!: FormGroup;

  constructor(
    private formBuilder: FormBuilder,
    private http: HttpClient,
    private router:Router
  ){}

  ngOnInit():void {
    this.form = this.formBuilder.group({
      email:'',
      password: ''
    });
  }

  submit():void {
    const headers = new HttpHeaders({ 'Content-Type': 'application/json' });
        const body = JSON.stringify(this.form.getRawValue());
    
        this.http.post('http://localhost:8000/api/login/',body, {headers,withCredentials:true})
          .subscribe(() => this.router.navigate(['/']))
  }
}

//withCredentials:true : to get the cookies from the backend