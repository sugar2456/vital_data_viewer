'use client';

import Link from 'next/link';
import { usePathname } from 'next/navigation';
import clsx from 'clsx';
import Calendar from '../commons/calendar';
import { FaFire, FaHome, FaMoon, FaRunning, FaUsers } from 'react-icons/fa';
import { FaBowlFood } from "react-icons/fa6";

const links = [
  { name: 'Home', href: '/dashboard', icon: FaHome },
  { name: 'sleep', href: '/dashboard/sleeps', icon: FaMoon },
  {
    name: 'Activity',
    href: '/dashboard/activity',
    icon: FaRunning,
  },
  { name: 'Calories', href: '/dashboard/calories', icon: FaFire },
  { name: 'Foods', href: '/dashboard/foods', icon: FaBowlFood },
  { name: 'Users', href: '/dashboard/users', icon: FaUsers },
];

export default function NavLinks() {
  const pathname = usePathname();
  return (
    <>
      {links.map((link) => {
        const LinkIcon = link.icon;
        return (
          <Link
            key={link.name}
            href={link.href}
            className={clsx(
              'flex h-[48px] grow items-center justify-center gap-2 rounded-md bg-gray-50 p-3 text-sm font-medium hover:bg-sky-100 hover:text-blue-600 md:flex-none md:justify-start md:p-2 md:px-3',
              {
                'bg-sky-100 text-blue-600': pathname === link.href,
              },
            )}
          >
            <LinkIcon className="w-7 h-7" />
            <p className="hidden md:block">{link.name}</p>
          </Link>
        );
      })}
      <div className='hidden md:block h-auto w-full'>
        <Calendar />
      </div>
    </>
  );
}