const cloneSymbol = Symbol('clone');

class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  get brand() {
    return this._brand;
  }

  get motor() {
    return this._motor;
  }

  get color() {
    return this._color;
  }

  cloneCar() {
    const clonedCar = new this.constructor();

    // Copy properties to the cloned object
    for (const key of Object.getOwnPropertyNames(this)) {
      if (key !== cloneSymbol) {
        clonedCar[key] = this[key];
      }
    }

    return clonedCar;
  }
}

export default Car;
