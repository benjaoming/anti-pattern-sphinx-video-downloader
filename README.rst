anti-pattern-sphinx-video-downloader
====================================

We want to be able to have videos in documentation. However, this project
should be considered an **anti-pattern** since it is discouraged to host
large files directly inside your Sphinx build outputs. Most hosted
solutions for Sphinx projects do not support large video files or are
likely to break such support if it becomes problematic.

   An anti-pattern in software engineering, project management, and
   business processes is a common response to a recurring problem that
   is usually ineffective and risks being highly
   counterproductive.[1][2] The term, coined in 1995 by computer
   programmer Andrew Koenig, was inspired by the book Design Patterns
   (which highlights a number of design patterns in software development
   that its authors considered to be highly reliable and effective) and
   first published in his article in the Journal of Object-Oriented
   Programming.[3] A further paper in 1996 presented by Michael Ackroyd
   at the Object World West Conference also documented anti-patterns.

https://en.wikipedia.org/wiki/Anti-pattern

Quick brainstorm
----------------

Here are the **disadvantages** of many different methods:

-  Youtube embeds: Commercials + tracking
-  Peertube embeds: Either run your own instance or use an instance
   that’s likely unrelated to your interests
-  Embeds in general: Do not play nicely with CSP, however Youtube might
   be universally allowed for hosted RTD
-  Embeds in general: Video takedowns often go un-noticed. That’s why
   embedded Youtube videos are often broken. Difficult to verify at
   documentation build time.
-  Git: Huge binary files in Git aren’t nice
-  Git LFS: Needs to be configured and added
-  Git LFS or dynamic downloads: Adds to build time
-  Git LFS: Do we even want to version a video file?
-  Dynamic downloads: Nice but we still need a source video available
   somewhere at build time

Here are some **advantages**:

-  Embeds: Multiple bitrates, once it has been created it should Just
   Work
-  Downloaded videos can break a build if they do not exist at build
   time.
-  Downloaded videos displayed with ``<video>`` are possible for users
   to save on their own device.
