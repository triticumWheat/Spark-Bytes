import React, { useState } from 'react';
import { Form, Input, Button, notification } from 'antd';
import axios from 'axios';

const Login = ({ onCancel }) => {
  const [loading, setLoading] = useState(false);
  
  const handleSubmit = (values) => {
    setLoading(true);
    axios.post('http://localhost:5001/login', values)
      .then((response) => {
        notification.success({
          message: 'Login Successful',
          description: 'You have logged in successfully.',
        });
        setLoading(false);
        onCancel();
      })
      .catch((error) => {
        notification.error({
          message: 'Login Failed',
          description: 'Invalid credentials, please try again.',
        });
        setLoading(false);
      });
  };

  return (
    <Form onFinish={handleSubmit}>
      <Form.Item
        name="username"
        rules={[{ required: true, message: 'Please enter your username!' }]}
      >
        <Input placeholder="Username" />
      </Form.Item>
      <Form.Item
        name="password"
        rules={[{ required: true, message: 'Please enter your password!' }]}
      >
        <Input.Password placeholder="Password" />
      </Form.Item>
      <Form.Item>
        <Button type="primary" htmlType="submit" block loading={loading}>
          Login
        </Button>
      </Form.Item>
    </Form>
  );
};

export default Login;
