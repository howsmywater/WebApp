import React, { Component } from 'react';
import styled from 'styled-components';

export default class CurrentLocation extends Component {
    componentDidMount() {
        navigator.geolocation.getCurrentPosition((position) => {
            const geolocation = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            this.props.didSetLocation(geolocation);
        });
    }

    render() {
        const CLWrap = styled.div`
            flex: 1;
            box-sizing: border-box;
            padding: 0.5rem;
            font-size: 1.2rem;
            display: flex;
            flex-direction: row;
            height: 100%;
            align-items: center;
        `;

        const Image = styled.img`
            height: 1em;
            margin-right: 8px;
        `;

        const Text = styled.span`
            font-family: 300;
        `;

        return (
            <CLWrap>
                <Image src="/static/currentLocation.svg"/>
                <Text>Current Location</Text>
            </CLWrap>
        );
    }
}
