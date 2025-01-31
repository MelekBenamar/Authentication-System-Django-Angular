import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Emitters } from '../emitters/emitters';

@Component({
  selector: 'app-home',
  standalone: false,
  
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})
export class HomeComponent {
  message ='';

  constructor(
    private http: HttpClient,
  ){}

  ngOnInit():void{
    this.http.get('http://localhost:8000/api/user/',{withCredentials:true}).subscribe((res:any) => {
      this.message = `Hi ${res.name}`;
      Emitters.authEmiiter.emit(true);
    },
  err => {
    this.message = 'You are not logged in!';
    Emitters.authEmiiter.emit(false);
  })
  }
}
