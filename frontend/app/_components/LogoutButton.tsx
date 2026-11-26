"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";
import { apiFetch } from "../_lib/client";
import ErrorList from "./ErrorList";

export default function LogoutButton() {
  const router = useRouter();
  const [errors, setErrors] = useState<string[]>([]);

  async function handleClick() {
    const result = await apiFetch("/api/auth/logout/", "POST");
    if (result.ok) {
      router.push("/login/");
      router.refresh();
      return;
    }
    setErrors(result.errors);
  }

  return (
    <>
      <ErrorList errors={errors} />
      <button type="button" onClick={handleClick}>
        ログアウト
      </button>
    </>
  );
}
