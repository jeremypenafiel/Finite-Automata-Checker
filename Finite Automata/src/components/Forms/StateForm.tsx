import React, { useState } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

const StateForm = () => {
  const [stateCounter, setStateCounter] = useState(0);

  const handleAddStateClick = () => {
    setStateCounter(stateCounter + 1);
  };
  const handleDeleteStateClick = () => {
    if (stateCounter === 0) {
      return;
    }
    setStateCounter(stateCounter - 1);
  };
  return (
    <Form.Group>
      <button type="button" onClick={handleAddStateClick}>
        Add State
      </button>
      <button type="button" onClick={handleDeleteStateClick}>
        Delete State
      </button>
      {Array.from(Array(stateCounter)).map((c, index) => {
        return (
          <Col>
            <InputGroup>
              <InputGroup.Text>State {index + 1}: </InputGroup.Text>
              <InputGroup.Text>Final State: </InputGroup.Text>
              <InputGroup.Checkbox
                name={`FinalState${index}`}
              ></InputGroup.Checkbox>
              <Form.Control
                readOnly
                disabled
                required
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
