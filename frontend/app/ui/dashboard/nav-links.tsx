'use client';
import {
  UserGroupIcon,
  HomeIcon,
  DocumentDuplicateIcon,
  MoonIcon,
} from '@heroicons/react/24/outline';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import clsx from 'clsx';
import Calendar from '../commons/calendar';

const links = [
  { name: 'Home', href: '/dashboard', icon: HomeIcon },
  { name: 'sleep', href: '/dashboard/sleeps', icon: MoonIcon },
  {
    name: 'Steps',
    href: '/dashboard/steps',
    icon: DocumentDuplicateIcon,
  },
  { name: 'Users', href: '/dashboard/users', icon: UserGroupIcon },
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
            <LinkIcon className="w-6" />
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