import React, { Component } from 'react';
import styled from 'styled-components';

export default class MapRoot extends Component {
    render() {
        const Container = styled.div`
            width: 60%;
            margin: 0 auto;
        `;

        const Header = styled.div`
            font-size: 25px;
        `;

        const FormRoot = styled.div`
            margin-top: 8px;
        `;

        const Label = styled.div`
            color: #AAA;
            text-transform: uppercase;
            font-size: 11px;
            font-weight: bold;
            letter-spacing: 1px;
        `;

        const Input = styled.input`
            width: 100%;
            border-radius: 4px;
            padding: 4px 8px;
            font-size: 18px;
            border: 1px solid #CCC;
            box-shadow: 0px 5px 8px -4px rgba(0, 0, 0, 0.2);
        `;

        const SplitRoot = styled.div`
            display: flex;

        `;

        return (
            <Container>
                <h4>Check your water quality</h4>
                <FormRoot>
                    <Label>Location</Label>
                    <Input/>
                </FormRoot>
                <SplitRoot>
                </SplitRoot>
            </Container>
        );
    }
}
