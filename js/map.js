import React, { Component } from 'react';
import WQResultView from './WQResultView';
import { Map as LeafletMap, TileLayer } from 'react-leaflet';
import styled from 'styled-components';

export default class MapRoot extends Component {
    state = {
        currentResult: null
    }

    render() {
        const Container = styled.div`
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
            width: 70%;
            height: 100%;
            margin: 0 auto;
        `;

        const Header = styled.div`
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 8px;
        `;

        const MapContainer = styled.div`
            width: 100%;
            height: 100%;
        `;

        return (
            <Container>
                <Header>Check your water quality</Header>
                <MapContainer>
                    <LeafletMap center={[37.87265302, -122.25963921]} zoom={8}>
                        <TileLayer
                          attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        />
                    </LeafletMap>
                </MapContainer>
            </Container>
        );
    }
}
