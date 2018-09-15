import React, { Component } from 'react';
import styled from 'styled-components';

export default class LocationIndicator extends Component {
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
                <Image src="/static/place.svg"/>
                <Text>{ this.props.name }</Text>
            </CLWrap>
        );
    }
}
