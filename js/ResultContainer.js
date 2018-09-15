import React, { Component } from 'react';
import { MapComponent } from 'react-leaflet';
import styled from 'styled-components';

export default class ResultContainer extends MapComponent {
    state = {
        station: null
    }

    render() {
        const ResultWrapper = styled.div`
            position: absolute;
            right: 16px;
            width: 300px;
            background: white;
            border-radius: 4px;
            z-index: 2000;
            margin-top: 70px;
            padding: 0.5rem 1rem;
            box-shadow: 0px 5px 16px -8px rgba(0, 0, 0, 0.5);
        `;

        const Header = styled.h2`
            font-weight: bold;
            font-size: 2rem;
            margin: 0;
        `;

        const Overview = styled.h3`
        color: rgba(0,0,0,0.4);
        font-size: 1.3rem;
        margin: 0;
        font-weight: 500;
        `;

        this.props.setStationCall(this);

        return (
            this.state.station ? (
                <ResultWrapper>
                    <Header>{ this.state.station.name }</Header>
                    <Overview>{ this.state.station.text }</Overview>
                </ResultWrapper>
            ) : <div/>
        );
    }

    setStation(station) {
        this.setState({ station: station })
    }
}
