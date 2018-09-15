import React, { Component } from 'react';
import WQResultView from './WQResultView';
import MapSearch from './MapSearch';
import L from 'leaflet';
import { Map as LeafletMap, TileLayer, Marker, Popup } from 'react-leaflet';
import styled from 'styled-components';

export default class MapRoot extends Component {
    constructor(props) {
        super(props);
        this.oldGroup = null;
    }

    render() {
        const Container = styled.div`
            width: 100%;
            height: 100%;
            box-sizing: border-box;
            margin: 0 auto;
            padding: 2rem;
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

        const icon = new L.divIcon({
            iconSize: L.point(40, 40, true),
            html: `<span>S</span>`
        });

        return (
            <Container>
                <Header>Check your water quality</Header>
                <MapContainer>
                    <LeafletMap
                        center={[37.87265302, -122.25963921]}
                        zoom={8}
                        maxZoom={300}
                        onMoveend={this.shouldUpdatePoints.bind(this)}
                        ref={map => this.map = map.leafletElement}>
                        <MapSearch
                            didSetLocation={this.didSetLocation}/>
                        <TileLayer
                          attribution="&amp;copy <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                          url="https://{s}.tile.thunderforest.com/transport-dark/{z}/{x}/{y}.png?apikey=db5ae1f5778a448ca662554581f283c5"
                          detectRetina={true} />
                    </LeafletMap>
                </MapContainer>
            </Container>
        );
    }

    didSetLocation = ({ lat, lng }) => {
        this.map.flyTo(new L.LatLng(lat, lng), 14);
    }

    /**
     * Loads the markers for a given latitude/longitude
     */
    shouldUpdatePoints(event) {
        const map = event.target;
        const center = map.getCenter();

        const stationIcon = L.divIcon({
            html: `<img src="/static/point.svg" />`,
            iconSize: [24, 24]
        })

        fetch(`/api/${center.lat}/${center.lng}`)
            .then(response => response.json())
            .then(({ stations }) => {

                // Remove old markers
                if (this.oldGroup) {
                    this.map.removeLayer(L.layerGroup);
                }

                const newMarkers = stations.map(
                    station => {
                        const marker = new L.Marker([station.latitude, station.longitude], {
                            className: 'point-style',
                            icon: stationIcon
                        });

                        marker.on('click', (event) => {
                            console.log(`Opening ${station}`, station);
                        });

                        return marker;
                });

                L.layerGroup(newMarkers).addTo(this.map);
            });
    }
}
