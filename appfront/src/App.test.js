import { render, screen } from '@testing-library/react';
import App from './App';

test('renders codMorse link', () => {
  render(<App />);
  const linkElement = screen.getByText(/codMorse/i);
  expect(linkElement).toBeInTheDocument();
});
