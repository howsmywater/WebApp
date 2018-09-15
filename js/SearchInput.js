import React, { Component } from 'react';
import styled from 'styled-components';

const Input = styled.input`
    padding: 0;
    margin: 0;
    border: none;
    outline: none;
    font-size: 1.6em;
    height: 100%;
    width: 100%;
`;

export default class CurrentLocation extends Component {

    componentDidMount() {
        this.autocomplete = new google.maps.places.Autocomplete(
            this.inputNode,
            { types: ['geocode'] }
        );

        this.autocomplete.addListener('place_changed', (event) => {
            const place = this.autocomplete.getPlace();
            const newLocation = place.geometry.location;
            this.props.didSetLocation({
                lat: newLocation.lat(),
                lng: newLocation.lng(),
                name: place.name
            });
        });
    }

    render() {
        this.input = <Input type='text' innerRef={input => this.inputNode = input}/>
        return (
            this.input
        );
    }

    shouldLoadResults = () => {

    }
}
