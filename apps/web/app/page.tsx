import Image from "next/image";
import { getUsers } from "../lib/api/users";
import { UserList } from "../components/UserList";
import { Suspense } from "react";

import { User } from "../types/user";

/**
 * Loading component for the user list.
 */
function UserListLoading() {
  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {[1, 2, 3].map((i) => (
        <div
          key={i}
          className="h-48 animate-pulse rounded-2xl bg-zinc-100 dark:bg-zinc-800"
        />
      ))}
    </div>
  );
}

/**
 * Root page component that fetches and displays users.
 */
export default async function Home() {
  let users: User[] = [];
  let error: string | null = null;

  try {
    users = await getUsers();
  } catch (e) {
    console.error("Error fetching users:", e);
    error = "Could not load users. Make sure the backend is running.";
  }

  return (
    <div className="min-h-screen bg-zinc-50 font-sans dark:bg-black">
      <header className="sticky top-0 z-10 border-b border-zinc-200 bg-white/80 backdrop-blur-md dark:border-zinc-800 dark:bg-black/80">
        <div className="mx-auto flex max-w-7xl h-16 items-center justify-between px-4 sm:px-6 lg:px-8">
          <div className="flex items-center gap-2">
            <Image
              className="dark:invert"
              src="/next.svg"
              alt="Trackly Logo"
              width={100}
              height={20}
              priority
            />
          </div>
          <nav className="flex items-center gap-4">
            <span className="text-sm font-medium text-zinc-500 dark:text-zinc-400">
              v0.1.0
            </span>
          </nav>
        </div>
      </header>

      <main className="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
        <div className="mb-12">
          <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 sm:text-5xl">
            Workspace Directory
          </h1>
          <p className="mt-4 text-lg text-zinc-600 dark:text-zinc-400">
            Manage your team and view all users connected to the Trackly platform.
          </p>
        </div>

        {error ? (
          <div className="rounded-2xl border border-red-200 bg-red-50 p-6 dark:border-red-900/50 dark:bg-red-900/20">
            <p className="text-red-800 dark:text-red-300 font-medium">{error}</p>
          </div>
        ) : (
          <Suspense fallback={<UserListLoading />}>
            <UserList users={users} />
          </Suspense>
        )}
      </main>

      <footer className="mx-auto max-w-7xl border-t border-zinc-200 px-4 py-8 dark:border-zinc-800 sm:px-6 lg:px-8">
        <p className="text-center text-sm text-zinc-500 dark:text-zinc-400">
          &copy; 2026 Trackly Inc. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
