"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { apiFetch } from "../_lib/client";
import ErrorList from "./ErrorList";

type Field = { name: string; label: string; type: "text" | "password"; autoComplete: string };

// ログインと登録で共通のフォーム
export default function AuthForm({
  action,
  fields,
  submitLabel,
}: {
  action: string;
  fields: Field[];
  submitLabel: string;
}) {
  const router = useRouter();
  const [errors, setErrors] = useState<string[]>([]);
  const [sending, setSending] = useState(false);

  async function handleSubmit(event: React.SyntheticEvent<HTMLFormElement>) {
    event.preventDefault();
    const data = Object.fromEntries(new FormData(event.currentTarget));
    setSending(true);
    const result = await apiFetch(action, "POST", data);
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
      {fields.map(({ label, ...input }) => (
        <p key={input.name}>
          <label>
            {label}: <input {...input} required />
          </label>
        </p>
      ))}
      <input type="submit" value={submitLabel} disabled={sending} />
    </form>
  );
}
