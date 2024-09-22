import { createFileRoute } from '@tanstack/react-router';
import AdjudicatorDashboard from '../components/Allocation/AdjudicatorDashboard';
import useAuth from '../hooks/useAuth';
// Define the route using createFileRoute
export const Route = createFileRoute('/adjudicator-dashboard')({
  component: AdjudicatorDashboard,
  // You can add optional route hooks like `beforeLoad` if needed
});

export default AdjudicatorDashboard;
