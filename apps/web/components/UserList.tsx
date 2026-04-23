import { User } from "../types/user";

interface UserListProps {
  users: User[];
}

/**
 * A premium component to display a list of users with avatars and details.
 */
export function UserList({ users }: UserListProps) {
  if (users.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-12 text-center bg-white/50 dark:bg-zinc-900/50 rounded-2xl border border-zinc-200 dark:border-zinc-800 backdrop-blur-sm">
        <p className="text-zinc-500 dark:text-zinc-400">No users found.</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-3">
      {users.map((user) => (
        <div
          key={user.id}
          className="group relative flex flex-col items-center gap-4 p-6 bg-white dark:bg-zinc-900 rounded-2xl border border-zinc-200 dark:border-zinc-800 transition-all hover:shadow-xl hover:shadow-zinc-200/50 dark:hover:shadow-zinc-950/50 hover:-translate-y-1"
        >
          <div className="relative h-16 w-16 overflow-hidden rounded-full border-2 border-zinc-100 dark:border-zinc-800">
            {user.profile_image_url ? (
              <img
                src={user.profile_image_url}
                alt={user.name}
                className="h-full w-full object-cover"
              />
            ) : (
              <div className="flex h-full w-full items-center justify-center bg-linear-to-br from-indigo-500 to-purple-600 text-xl font-bold text-white">
                {user.name.charAt(0)}
              </div>
            )}
          </div>
          <div className="text-center">
            <h3 className="text-lg font-semibold text-zinc-900 dark:text-zinc-50">
              {user.name}
            </h3>
            <p className="text-sm text-zinc-500 dark:text-zinc-400">
              {user.email}
            </p>
          </div>
          <div className="mt-2 flex items-center gap-2">
            <span className="inline-flex items-center rounded-full bg-indigo-50 px-2 py-1 text-xs font-medium text-indigo-700 dark:bg-indigo-900/30 dark:text-indigo-400">
              User
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}
