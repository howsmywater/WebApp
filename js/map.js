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
            width: 70%;
            height: 100%;
            box-sizing: border-box;
            margin: 0 auto;
            padding: 2rem 0;
            display: flex;
            flex-direction: column;
        `;

        const Header = styled.div`
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 8px;
        `;

        const MapContainer = styled.div`
            width: 100%;
            flex: 1;
            overflow: hidden;
            border-radius: 4px;
            border-radius: 8px;
            position: relative;
            z-index: 500;
            box-shadow: 0px 5px 16px -8px rgba(0, 0, 0, 0.5);
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
