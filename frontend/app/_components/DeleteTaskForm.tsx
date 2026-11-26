"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { apiFetch } from "../_lib/client";
import type { Task } from "../_lib/types";
import ErrorList from "./ErrorList";

export default function DeleteTaskForm({ task }: { task: Task }) {
  const router = useRouter();
  const [errors, setErrors] = useState<string[]>([]);

  async function handleSubmit(event: React.SyntheticEvent<HTMLFormElement>) {
    event.preventDefault();
    const result = await apiFetch(`/api/tasks/${task.id}/`, "DELETE");
    if (result.ok) {
      router.push("/");
      router.refresh();
      return;
    }
    setErrors(result.errors);
  }

  return (
    <form onSubmit={handleSubmit}>
      <ErrorList errors={errors} />
      <p>
        Is it ready to delete &quot;{task.title} ({task.description ?? ""})&quot;?
      </p>
      <input type="submit" value="Delete" />
    </form>
  );
}
