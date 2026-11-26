"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { apiFetch } from "../_lib/client";
import type { Task } from "../_lib/types";
import ErrorList from "./ErrorList";

// task があれば編集、なければ作成
export default function TaskForm({ task }: { task?: Task }) {
  const router = useRouter();
  const [errors, setErrors] = useState<string[]>([]);
  const [sending, setSending] = useState(false);

  async function handleSubmit(event: React.SyntheticEvent<HTMLFormElement>) {
    event.preventDefault();
    const form = new FormData(event.currentTarget);
    setSending(true);
    const result = await apiFetch(
      task ? `/api/tasks/${task.id}/` : "/api/tasks/",
      task ? "PATCH" : "POST",
      {
        title: form.get("title"),
        description: form.get("description"),
        completed: form.get("completed") === "on",
      },
    );
    if (result.ok) {
      router.push("/");
      router.refresh();
      return;
    }
    setErrors(result.errors);
    setSending(false);
  }

  return (
    <form onSubmit={handleSubmit}>
      <ErrorList errors={errors} />
      <p>
        <label>
          Title: <input name="title" defaultValue={task?.title} maxLength={255} required />
        </label>
      </p>
      <p>
        <label>
          Description:{" "}
          <textarea name="description" defaultValue={task?.description ?? ""} cols={40} rows={10} />
        </label>
      </p>
      <p>
        <label>
          Completed: <input type="checkbox" name="completed" defaultChecked={task?.completed} />
        </label>
      </p>
      <input type="submit" value="Save!" disabled={sending} />
    </form>
  );
}
