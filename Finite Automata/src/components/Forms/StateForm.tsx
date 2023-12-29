import React, { useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";
import Fade from "react-bootstrap/Fade";

interface StateFormProps {
  stateCount: number;
}

const StateForm: React.FC<StateFormProps> = ({ stateCount }) => {
  return (
    <Form.Group>
      {Array.from(Array(stateCount)).map((c, index) => {
        return (
          <Col key={index}>
            <InputGroup>
              <InputGroup.Text>State {index + 1}: </InputGroup.Text>
              <InputGroup.Text>Final State: </InputGroup.Text>
              <InputGroup.Checkbox
                name={`FinalState${index}`}
              ></InputGroup.Checkbox>
              <Form.Control
                readOnly
                required
                value={`q${index}`}
                placeholder={`q${index}`}
                name={`State${index}`}
              />
            </InputGroup>
          </Col>
        );
      })}
    </Form.Group>
  );
};

export default StateForm;
