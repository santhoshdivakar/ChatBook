"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var Hero = (function () {
    function Hero() {
    }
    return Hero;
}());
exports.Hero = Hero;
var HEROES = [
    { id: 2, name: 'Superman' },
    { id: 3, name: 'Spiderman' },
    { id: 4, name: 'Dr Strange' },
    { id: 5, name: 'Magneto' },
];
var AppComponent = (function () {
    function AppComponent() {
        this.title = 'Angular Heroes';
    }
    AppComponent = __decorate([
        core_1.Component({
            selector: 'my-app',
            template: '
                < h2 > Angular, Heroes: function () { } } / h2 >
            (function () {
                function class_1() {
                }
                return class_1;
            }()), "heroes" >
             * ngFor, "let hero of heroes" >
            (function () {
                function class_2() {
                }
                return class_2;
            }()), "badge" > {}, { hero: .id }, /span> {{hero.name}}
            < /li>
            < /ul>'), 
        __metadata('design:paramtypes', [])
    ], AppComponent);
    return AppComponent;
}());
exports.AppComponent = AppComponent;
//# sourceMappingURL=app.component.js.map