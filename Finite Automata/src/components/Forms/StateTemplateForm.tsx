import React from "react";
import Col from "react-bootstrap/Col";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

interface StateTemplateFormProps {
  index: number;
  finalState: string;
}

const StateTemplateForm: React.FC<StateTemplateFormProps> = ({
  index,
  finalState,
}) => {
  return (
    <Col>
      <InputGroup>
        <InputGroup.Text>State {index + 1}: </InputGroup.Text>
        <InputGroup.Text>Final State: </InputGroup.Text>
        <InputGroup.Checkbox
          readOnly
          checked={finalState === "on" ? true : false}
          name={`FinalState${index}`}
        ></InputGroup.Checkbox>
        <Form.Control
          readOnly
          value={`q${index}`}
          placeholder={`q${index}`}
          name={`State${index}`}
        />
      </InputGroup>
    </Col>
  );
};

export default StateTemplateForm;
