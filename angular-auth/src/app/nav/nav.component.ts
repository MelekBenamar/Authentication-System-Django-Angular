import { Component } from '@angular/core';
import { Emitters } from '../emitters/emitters';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-nav',
  standalone: false,
  
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {

  authenticated= false;
  constructor(private http: HttpClient){}

  ngOnInit():void {
    Emitters.authEmiiter.subscribe(
      (auth: boolean) => {
        this.authenticated=auth;
      }
    )
  }

  logout(): void {
    this.http.post('http://localhost:8000/api/logout/',{},{withCredentials:true})
      .subscribe(() => this.authenticated=false)
  }
}
