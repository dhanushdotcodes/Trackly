import { User } from "../../types/user";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

/**
 * Fetches all users from the backend API.
 * @returns A promise that resolves to an array of User objects.
 */
export async function getUsers(): Promise<User[]> {
  const response = await fetch(`${API_URL}/users/`, {
    cache: "no-store", // Ensure we get fresh data
  });

  if (!response.ok) {
    throw new Error(`Failed to fetch users: ${response.statusText}`);
  }

  return response.json();
}
