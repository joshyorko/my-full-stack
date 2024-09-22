import React from 'react';
import { Clock } from 'lucide-react';
import useAuth from '../hooks/useAuth'; // Adjust this import based on your actual auth hook

// ... (keep all the existing interfaces and components)

function AdjudicatorDashboard() {
  // ... (keep all the existing component logic)
}

// Export the Route object
export const Route = {
  component: AdjudicatorDashboard,
  // Add any additional route properties here if needed
  // For example:
  // loader: () => { /* ... */ },
  // action: () => { /* ... */ },
};

// Also export the component as default for flexibility
export default AdjudicatorDashboard;