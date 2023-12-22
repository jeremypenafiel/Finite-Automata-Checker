import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import InputGroup from "react-bootstrap/InputGroup";

interface TransitionFunctionFormProps {
  stateCount: number;
}

const TransitionFunctionForm: React.FC<TransitionFunctionFormProps> = ({
  stateCount,
}) => {
  const [ruleCounter, setRuleCounter] = useState(0);

  const handleAddRuleClick = () => {
    setRuleCounter(ruleCounter + 1);
    console.log(ruleCounter);
  };
  const handleDeleteRuleClick = () => {
    if (ruleCounter === 0) {
      return;
    }
    setRuleCounter(ruleCounter - 1);
    console.log(ruleCounter);
  };
  return (
    <Form.Group>
      <button type="button" onClick={handleAddRuleClick}>
        Add Rule
      </button>
      <button type="button" onClick={handleDeleteRuleClick}>
        Delete Rule
      </button>
      {Array.from(Array(ruleCounter)).map((c, index) => {
        return (
          <InputGroup>
            <InputGroup.Text>Rule {index + 1}: </InputGroup.Text>
            {/* <Form.Control
              required
              placeholder="Current State"
              name={`CurrentState ${index}`}
            /> */}
            <Form.Select>
              {Array.from(Array(stateCount)).map((c, index) => {
                return <option>q{index}</option>;
              })}
            </Form.Select>
            <Form.Control
              required
              placeholder="Input symbol"
              name={`InputSymbol ${index}`}
            />
            <Form.Control
              required
              placeholder="Stack Top"
              name={`StackTop ${index}`}
            />
            <Form.Control
              required
              placeholder="next state"
              name={`NextState ${index}`}
            />
            <Form.Control
              required
              placeholder="stack push"
              name={`StackPush ${index}`}
            />
          </InputGroup>
        );
      })}
    </Form.Group>
  );
};

export default TransitionFunctionForm;
