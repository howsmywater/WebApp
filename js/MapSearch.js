import React, { Component } from 'react';
import styled from 'styled-components';
import CurrentLocation from './CurrentLocation';
import SearchInput from './SearchInput';
import LocationIndicator from './LocationIndicator';
import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';
import { MapComponent } from 'react-leaflet';

export default class MapSearch extends MapComponent {
    state = {
        isCurrentLocation: true,
        isEntering: false
    }

    render() {
        const SearchWrapper = styled.div`
            background: white;
            border-radius: 4px;
            position: absolute;
            top: 8px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            flex-direction: row;
            width: 800px;
            z-index: 1000;
            margin: 0 auto;
            height: 3rem;
            box-sizing: border-box;
            padding: 0.5rem 1rem;
            box-shadow: 0px 4px 12px -4px rgba(0, 0, 0, 0.3);

            > img {
                height: 2.5em;
                width: 2.5em;
            }
        `;

        const SearchContent = styled.div`
            flex: 1;
            margin-left: 16px;
        `;

        return (
            <SearchWrapper>
                <img src="/static/search.svg"/>
                <SearchContent>
                    { this.state.isEntering ?
                        <SearchInput
                            didSetLocation={this.didSetLocation.bind(this, false)} /> :
                        this.state.isCurrentLocation ?
                        <CurrentLocation
                            didSetLocation={this.didSetLocation.bind(this, true)} /> :
                        <LocationIndicator
                            name={this.state.name} /> }
                </SearchContent>
                <img onClick={this.setEntering.bind(this)} src="/static/close.svg"/>
            </SearchWrapper>
        );
    }

    /**
     * Sets the state to entering
     */
    setEntering() {
        this.setState({ isEntering: true, isCurrentLocation: false });
    }

    /**
     * Called when location set
     */
    didSetLocation(isCurrent, { lat, lng, name = null }) {
        this.setState({
            isCurrentLocation: isCurrent,
            isEntering: false,
            name: name
        });

        this.props.didSetLocation({ lat, lng })
    }
}
