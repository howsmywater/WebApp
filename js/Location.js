/**
 * Represents location
 */
export default class Location {
    constructor({ lat, lng }) {
        this.lat = lat;
        this.lng = lng;
    }

    asArray() {
        return [this.lat, this.lng];
    }

    asJSON() {
        return {
            lat: this.lat,
            lng: this.lng
        }
    }
}
