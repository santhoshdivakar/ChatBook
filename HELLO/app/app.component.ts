import { Component } from '@angular/core';
export class Hero {
  id: number;
  name: string;
}
const HEROES: Hero[] = [
  { id: 2, name: 'Superman' },
  { id: 3, name: 'Spiderman' },
  { id: 4, name: 'Dr Strange' },
  { id: 5, name: 'Magneto' },
];

@Component({
  selector: 'my-app',
  template:'
      <h2>Angular Heroes</h2>
      <ul class="heroes">
          <li *ngFor="let hero of heroes">
              <span class="badge">{{hero.id}}</span> {{hero.name}}
          </li>
      </ul>'
})
export class AppComponent {
  title = 'Angular Heroes';
  heroes: HEROES;
}

